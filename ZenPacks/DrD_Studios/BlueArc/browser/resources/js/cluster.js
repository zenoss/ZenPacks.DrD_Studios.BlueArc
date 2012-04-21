(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName('BlueArcClusterNode', _t('Cluster Node'), _t('Cluster Nodes'));

Ext.apply(Zenoss.render, {
    checkbox: function(bool) {
        if (bool) {
            return '<input type="checkbox" checked="true" disabled="true">';
        } else {
            return '<input type="checkbox" disabled="true">';
        }
    }
});

ZC.BlueArcClusterNodePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'name',
            componentType: 'BlueArcClusterNode',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'node_id'},
                {name: 'node_ip'},
                {name: 'managed_device'},
                {name: 'node_status'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'node_id',
                dataIndex: 'node_id',
                header: _t('Node ID'),
                sortable: true,
                width: 80
            },{
                id: 'node_ip',
                dataIndex: 'node_ip',
                header: _t('IP Address'),
                sortable: true,
                width: 80
            },{
                id: 'managed_device',
                dataIndex: 'managed_device',
                header: _t('Managed Device'),
                renderer: function(obj) {
                    if (obj && obj.uid && obj.name) {
                        return Zenoss.render.link(obj.uid, undefined, obj.name);
                    }
                },
                width: 140
            },{
                id: 'node_status',
                dataIndex: 'node_status',
                header: _t('Status'),
                sortable: true,
                width: 80
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.BlueArcClusterNodePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('BlueArcClusterNodePanel', ZC.BlueArcClusterNodePanel);

})();
