import Globals

from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused

unused(Globals)


class ZenPack(ZenPackBase):
    def install(self, app):
        """Custom install method for this ZenPack."""
        self.pre_install(app)
        super(ZenPack, self).install(app)

    def pre_install(self, app):
        """Perform steps that should be done before default install."""
        devices = app.zport.dmd.Devices

        # /Storage device class is a prerequisite.
        devices.createOrganizer('/Storage')
