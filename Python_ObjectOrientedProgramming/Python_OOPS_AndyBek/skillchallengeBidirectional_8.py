

from collections import UserDict

class BidirectionalDict(UserDict):
    #bd['a'] = 'b'
    # a->b, b->a

    # del bd['a']
    # both b-> a and a-> b are removed.

    def __setitem__(self, key, value):

        if key in self:
            del self[key]

        if value in self:
            del self[value]
        
        # for each binding we creating two entries.
        super().__setitem__(key, value)
        super().__setitem__(value, key)

    def __len__(self):
        return super().__len__() // 2
    
    def __delitem__(self, key):
        super().__delitem__(self[key])
        super().__delitem__(key)

    #  POP and Update should work as expected.
    

    
