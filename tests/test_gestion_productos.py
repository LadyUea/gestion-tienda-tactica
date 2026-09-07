import unittest
from src.gestion_productos.producto import Producto


class TestProducto(unittest.TestCase):

    def test_producto_con_stock(self):
        producto = Producto("Mochila tactica", 35.0, 5)
        self.assertTrue(producto.tiene_stock())

    def test_producto_sin_stock(self):
        producto = Producto("Linterna", 20.0, 0)
        self.assertFalse(producto.tiene_stock())


if __name__ == "__main__":
    unittest.main()
