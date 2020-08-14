'''Contains implemntation of the obsesrver pattern.
'''

from abc import ABC, abstractmethod


class Observable():
    '''Class that alerts the observers of changes.

    Don't use attach and detach outside of init and remove

    Attributes
    ----------

    observers : list
        a list of the objects alerted when observable notified


    Methods
    -------

    attach(observer):
        Adds observer to observable list

    detach(observer):
        Removes observer from observable list

    notify():
        Notifies all observers about an event
    '''

    observers = []

    def attach(self, observer):
        '''Adds observer to observable list
        '''
        self.observers.append(observer)

    def detach(self, observer):
        '''Removes observer from observable list
        '''
        self.observers.remove(observer)

    def notify(self):
        '''Notifies all observers about an event
        '''
        for observer in self.observers:
            observer.update(self)


class Observer(ABC):
    '''The observer interface that provides the update method

    Attributes
    ----------

    observable : Observable
        for attachment, detachment and getting data from the observable

    Methods
    -------

    remove():
        Detachs the observer from the observable

    update():
        Sends update to observers
    '''

    def __init__(self, observerable):
        self.observable = observable
        observable.attach(self)

    def remove(self):
        '''Removes the observer from the observable
        '''
        self.observable.detach(self)

    @abstractmethod
    def update(self, subject):
        ''' Recieves update from observerable
        '''
        pass

# class Concrete(Observer):
#     def update(self, subject):
#         print('Reacting')


# # Test
# if __name__ == '__main__':
#     observable = Observable()
#     concrete = Concrete(observable)
#     concrete2 = Concrete(observable)
#     concrete2.remove()
#     observable.notify()
#     while True:
        pass
