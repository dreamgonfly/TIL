# Dummy, Fake, Stubs, Spies, Mocks

**Test Double (think stunt double)** is a generic term for any case where you replace a production object for testing purposes. There are various kinds of double:

- **Dummy** objects are passed around but never actually used. Usually they are just used to fill parameter lists.
- **Fake** objects actually have working implementations, but usually take some shortcut which makes them not suitable for production (an [InMemoryTestDatabase](https://www.martinfowler.com/bliki/InMemoryTestDatabase.html) is a good example).
- **Stubs** provide canned answers to calls made during the test, usually not responding at all to anything outside what's programmed in for the test.
- **Spies** are stubs that also record some information based on how they were called. One form of this might be an email service that records how many messages it was sent.
- **Mocks** are pre-programmed with expectations which form a specification of the calls they are expected to receive. They can throw an exception if they receive a call they don't expect and are checked during verification to ensure they got all the calls they were expecting.

# Stubs vs. Mocks

## State verification

State verification means that we determine whether the exercised method worked correctly by examining the state of the **SUT(System Under Test)** and its collaborators after the method was exercised.

With state verification we verify that the order did the right thing in its interaction with the warehouse by asserts against the warehouse's state. 

### Drawback

In order to use state verification on the stub, I need to make some extra methods on the stub to help with verification.

## Behavior verification

Behavior verification means that we check to see if the SUT made the correct calls on the collaborators. Mocks use behavior verification.

With behavior verification, we tell the mock what to expect during setup and asking the mock to verify itself during verification. Only the order is checked using asserts, and if the method doesn't change the state of the order there's no asserts at all.

Of the kinds of doubles above, only mocks insist upon behavior verification.

    public class OrderInteractionTester extends MockObjectTestCase {
      private static String TALISKER = "Talisker";
    
      public void testFillingRemovesInventoryIfInStock() {
        //setup - data
        Order order = new Order(TALISKER, 50);
        Mock warehouseMock = new Mock(Warehouse.class);
        
        //setup - expectations
        warehouseMock.expects(once()).method("hasInventory")
          .with(eq(TALISKER),eq(50))
          .will(returnValue(true));
        warehouseMock.expects(once()).method("remove")
          .with(eq(TALISKER), eq(50))
          .after("hasInventory");
    
        //exercise
        order.fill((Warehouse) warehouseMock.proxy());
        
        //verify
        warehouseMock.verify();
        assertTrue(order.isFilled());
      }

### Drawback

When you write a mockist test, you are testing the outbound calls of the SUT to ensure it talks properly to its suppliers. Mockist tests are thus more coupled to the implementation of a method. Changing the nature of calls to collaborators usually cause a mockist test to break.

This coupling leads to a couple of concerns. The most important one is the effect on Test Driven Development. With mockist testing, writing the test makes you think about the implementation of the behavior - indeed mockist testers see this as an advantage. Classicists, however, think that it's important to only think about what happens from the external interface and to leave all consideration of implementation until after you're done writing the test.

Coupling to the implementation also interferes with refactoring, since implementation changes are much more likely to break tests than with classic testing.

# Reference

[bliki: TestDouble](https://www.martinfowler.com/bliki/TestDouble.html)

[Mocks Aren't Stubs](https://www.martinfowler.com/articles/mocksArentStubs.html)