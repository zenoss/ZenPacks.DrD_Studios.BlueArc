from zope.interface import implements

from Products.Zuul.decorators import info
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.DrD_Studios.BlueArc.interfaces import IClusterNodeInfo


class ClusterNodeInfo(ComponentInfo):
    """ClusterNode API (Info) adapter factory."""

    implements(IClusterNodeInfo)

    node_id = ProxyProperty('nodeID')
    node_ip = ProxyProperty('nodeIP')
    node_status = ProxyProperty('nodeStatus')

    @property
    @info
    def managed_device(self):
        return self._object.getManagedDevice()
