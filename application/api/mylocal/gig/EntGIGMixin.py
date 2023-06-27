from application.api.mylocal.gig.GIGTable import GIGTable


class EntGIGMixin:
    def gig(self, gig_table: GIGTable):
        return gig_table.get(self.id)
