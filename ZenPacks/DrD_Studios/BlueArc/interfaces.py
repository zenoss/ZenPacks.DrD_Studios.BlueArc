from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t


class IClusterNodeInfo(IComponentInfo):
    """Interface for ClusterNode API (Info) adapter."""

    node_id = schema.Int(title=_t(u'Node ID'))
    node_ip = schema.TextLine(title=_t(u'Node IP Address'))
    node_status = schema.TextLine(title=_t(u'Node Status'))
