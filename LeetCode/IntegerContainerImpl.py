from integer_container import IntegerContainer

class IntegerContainerImpl(IntegerContainer):

    def __init__(self):
        # TODO: implement
        self.container = []
        pass

    # TODO: implement interface methods here
    def add(self, number):
        self.container.append(number)
        return len(self.container)
   
    def delete(self, number):
     
        if number in self.container:
            while number in self.container:
                index = self.container.index(number)
                self.container.pop(index)
            return True             
        else:
            return False


# self.assertEqual(self.container.add(5), 1)
# self.assertEqual(self.container.add(10), 2)
# self.assertEqual(self.container.add(5), 3)
# self.assertTrue(self.container.delete(10))
# self.assertFalse(self.container.delete(1))
# self.assertEqual(self.container.add(1), 3)

container = IntegerContainerImpl()

print(container.add(5), container.container)
print(container.add(10), container.container)
print(container.add(5), container.container)
print(container.delete(10), container.container)
print(container.delete(1), container.container)
print(container.add(1), container.container)
