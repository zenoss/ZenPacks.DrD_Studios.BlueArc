from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE


class ClusterNode(DeviceComponent, ManagedEntity):
    """BlueArc Cluster Node Information"""

    portal_type = meta_type = 'BlueArcClusterNode'

    nodeID = None
    nodeIP = None
    nodeStatus = None

    _properties = ManagedEntity._properties + (
        {'id': 'nodeID', 'type': 'int', 'mode': 'w'},
        {'id': 'nodeIP', 'type': 'string', 'mode': 'w'},
        {'id': 'nodeStatus', 'type': 'string', 'mode': 'w'},
        )

    _relations = ManagedEntity._relations + (
        ('cluster', ToOne(ToManyCont,
            'ZenPacks.DrD_Studios.BlueArc.Cluster',
            'nodes')),
        )

    # This makes the "Templates" component display available.
    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

    def device(self):
        return self.cluster()

    def getManagedDevice(self):
        """Return a Zenoss managed device that matches this cluster node."""
        return self.findDevice(self.title)

    def snmpIgnore(self):
        return super(ClusterNode, self).snmpIgnore() or self.snmpindex < 0
