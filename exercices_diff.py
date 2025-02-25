# Max liste
def max_liste(liste):
    max_val = liste[0]
    for num in liste:
        if num > max_val:
            max_val = num
    return max_val

print(max_liste([3, 7, 2, 9, 5]))  # 9

# ----------------------------
# Trouver le deuxième plus grand
#def deuxieme_max_liste(liste):


import unittest

class TestMaxListe(unittest.TestCase):

    def test_max_liste(self):
        self.assertEqual(max_liste([3, 7, 2, 9, 5]), 9)
        self.assertEqual(max_liste([-3, -7, -2, -9, -5]), -2)
        self.assertEqual(max_liste([5]), 5)
        self.assertEqual(max_liste([0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()