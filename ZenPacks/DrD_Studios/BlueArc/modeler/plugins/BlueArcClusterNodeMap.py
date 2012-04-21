from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetTableMap


class BlueArcClusterNodeMap(SnmpPlugin):
    maptype = "BlueArcClusterNodesMap"
    relname = "nodes"
    modname = 'ZenPacks.DrD_Studios.BlueArc.ClusterNode'

    columns = {
        '.1': 'snmpindex',
        '.1': 'nodeID',
        '.2': 'nodeName',
        '.3': 'nodeIP',
        '.4': 'nodeStatus',
        }

    snmpGetTableMaps = (
        GetTableMap('node',
            '.1.3.6.1.4.1.11096.6.1.1.1.2.5.9.1',
            columns),
        )

    def process(self, device, results, log):
        log.info('processing %s for device %s', self.name(), device.id)

        rm = self.relMap()

        for snmpindex, row in results[1].get('node', {}).items():
            name = row.get('nodeName')
            if not name:
                continue

            om = self.objectMap()
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex.strip('.')
            om.nodeID = row.get('nodeID')
            om.nodeIP = row.get('nodeIP')
            om.nodeStatus = row.get('nodeStatus')

            rm.append(om)

        return rm
