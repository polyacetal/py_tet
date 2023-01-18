import Viewer
import Model

viewer = Viewer.Viewer()
model = Model.Model()
viewer.setField(model.getField())
viewer.PrintBlock()