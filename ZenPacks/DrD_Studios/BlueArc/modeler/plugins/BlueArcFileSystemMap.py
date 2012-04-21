from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetTableMap


class BlueArcFileSystemMap(SnmpPlugin):
    maptype = "BlueArcFileSystemMap"
    compname = "os"
    relname = "filesystems"
    modname = "Products.ZenModel.FileSystem"

    volumeCapacity = ''
    volumeFreeCapacity = ''

    columns = {
        '.3': 'volumeLabel',
        '.5': 'volumeCapacity',
        }

    snmpGetTableMaps = (
        GetTableMap('volumeTable',
            '.1.3.6.1.4.1.11096.6.1.1.1.3.5.2.1',
            columns),
    )

    def process(self, device, results, log):
        log.info('processing %s for device %s', self.name(), device.id)

        rm = self.relMap()
        for snmpindex, fs in results[1].get('volumeTable', {}).items():
            name = fs.get('volumeLabel')
            if not name:
                continue

            volumeCapacity = fs.get('volumeCapacity', 0)

            # Create the object map which puts our SNMP stats into the
            # FileSystem object
            om = self.objectMap()
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex.strip('.')
            om.mount = name
            om.type = '.1.3.6.1.2.1.25.2.1.4'
            om.blockSize = 1024
            om.totalBlocks = volumeCapacity / 1024

            rm.append(om)

        return rm
