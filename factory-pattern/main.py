from shape_factory import ShapeFactory

def main():
    shape_factory = ShapeFactory()

    shape1 = shape_factory.get_shape('Circle')
    shape1.draw()

    shape2 = shape_factory.get_shape('Rectangle')
    shape2.draw()

    shape3 = shape_factory.get_shape('Square')
    shape3.draw()

main()
