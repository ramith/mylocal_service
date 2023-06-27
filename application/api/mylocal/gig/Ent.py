from application.api.mylocal.gig.EntBase import EntBase
from application.api.mylocal.gig.EntGeoMixin import EntGeoMixin
from application.api.mylocal.gig.EntGIGMixin import EntGIGMixin
from application.api.mylocal.gig.EntJSONMixin import EntJSONMixin
from application.api.mylocal.gig.EntLoadMixin import EntLoadMixin


class Ent(EntBase, EntJSONMixin, EntLoadMixin, EntGIGMixin, EntGeoMixin):
    pass
