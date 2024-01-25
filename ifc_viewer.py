from OCC.Display.WebGl.jupyter_renderer import JupyterRenderer as Renderer

class ifc_viewer(Renderer):
    def __init__(self):
        Renderer.__init__(self)
        self.n = 0
        self.products = {}

    @staticmethod
    def subshapes(shp):
        import OCC.Core.TopoDS
        it = OCC.Core.TopoDS.TopoDS_Iterator(shp)
        while it.More():
            yield it.Value()
            it.Next()

    def Add(self, product, shp, color):
        for shp, sty in zip(self.subshapes(shp), color):
            Renderer.DisplayShape(self, shp, shape_color=sty[0:3], render_edges=True)
            self.products[shp] = product

    def click(self, item):
        Renderer.click(self, item)
        obj = item.owner.object
        if obj is not None:
            self.html.value = self.products[self._shapes[obj.name]].to_string()

