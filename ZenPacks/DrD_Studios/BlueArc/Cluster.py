from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class Cluster(Device):
    """BlueArc Cluster"""
    meta_type = portal_type = "BlueArcCluster"

    _relations = Device._relations + (
        ('nodes', ToManyCont(ToOne,
            'ZenPacks.DrD_Studios.BlueArc.ClusterNode',
            'cluster')),
        )
