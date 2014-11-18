package funsets

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

/**
 * This class is a test suite for the methods in object FunSets. To run
 * the test suite, you can either:
 *  - run the "test" command in the SBT console
 *  - right-click the file in eclipse and chose "Run As" - "JUnit Test"
 */
@RunWith(classOf[JUnitRunner])
class FunSetSuite extends FunSuite {


  /**
   * Link to the scaladoc - very clear and detailed tutorial of FunSuite
   *
   * http://doc.scalatest.org/1.9.1/index.html#org.scalatest.FunSuite
   *
   * Operators
   *  - test
   *  - ignore
   *  - pending
   */

  /**
   * Tests are written using the "test" operator and the "assert" method.
   */
  test("string take") {
    val message = "hello, world"
    assert(message.take(5) == "hello")
  }

  /**
   * For ScalaTest tests, there exists a special equality operator "===" that
   * can be used inside "assert". If the assertion fails, the two values will
   * be printed in the error message. Otherwise, when using "==", the test
   * error message will only say "assertion failed", without showing the values.
   *
   * Try it out! Change the values so that the assertion fails, and look at the
   * error message.
   */
  test("adding ints") {
    assert(1 + 2 === 3)
  }

  
  import FunSets._

  test("contains is implemented") {
    assert(contains(x => true, 100))
  }
  
  /**
   * When writing tests, one would often like to re-use certain values for multiple
   * tests. For instance, we would like to create an Int-set and have multiple test
   * about it.
   * 
   * Instead of copy-pasting the code for creating the set into every test, we can
   * store it in the test class using a val:
   * 
   *   val s1 = singletonSet(1)
   * 
   * However, what happens if the method "singletonSet" has a bug and crashes? Then
   * the test methods are not even executed, because creating an instance of the
   * test class fails!
   * 
   * Therefore, we put the shared values into a separate trait (traits are like
   * abstract classes), and create an instance inside each test method.
   * 
   */

  trait TestSets {
    val s1 = singletonSet(1)
    val s2 = singletonSet(2)
    val s3 = singletonSet(3)
    val s4 = singletonSet(4)
    val s5 = singletonSet(5)
    val s0 = singletonSet(0)
    val t1 = singletonSet(1)
    val t2 = singletonSet(2)
    val t3 = singletonSet(3)
    val u12 = union(s1, s2)
    val u23 = union(s2, s3)
    val u14 = union(s1, s4)
    val u45 = union(s4, s5)
    val u01 = union(s0, s1)
  }

  /**
   * This test is currently disabled (by using "ignore") because the method
   * "singletonSet" is not yet implemented and the test would fail.
   * 
   * Once you finish your implementation of "singletonSet", exchange the
   * function "ignore" by "test".
   */
  test("singletonSet(1) contains 1") {
    
    /**
     * We create a new instance of the "TestSets" trait, this gives us access
     * to the values "s1" to "s3". 
     */
    new TestSets {
      /**
       * The string argument of "assert" is a message that is printed in case
       * the test fails. This helps identifying which assertion failed.
       */
      assert(contains(s2, 2), "Singleton")
      assert(!contains(s1, 3), "Singleton")
    }
  }

  test("union contains all elements") {
    new TestSets {
      val s = union(s1, s2)
      assert(contains(s, 1), "Union 1")
      assert(contains(s, 2), "Union 2")
      assert(!contains(s, 3), "Union 3")
    }
  }
  
  test("intersection contains common elements") {
    new TestSets {
      val a = intersect(s2, t2)
      val b = intersect(s1, t3)
      assert(!contains(a, 1), "Intersection 1")
      assert(contains(a, 2), "Intersection 2")
      assert(!contains(b, 3), "Intersection 3")
    }
  }
  
  test("diff contains elements in first set but not in second set") {
    new TestSets {
      val a = diff(u12, u23)
      assert(contains(a, 1), "Diff 1")
      assert(!contains(a, 2), "Diff 2")
      assert(!contains(a, 3), "Diff 3")
    }
  }

  test("filter - returns subset of elements that satisfy the predicate") {
    new TestSets {
      val a = (x:Int) => (x < 3)
      val b = filter(u12, a)
      assert(contains(b, 1), "Filter 1")
      assert(contains(b, 2), "Filter 2")
      assert(!contains(b, 3), "Filter 3")
    }
  }
  
  test("forall - returns true if all elements in S satisfy predicate p") {
    new TestSets {
      val p1 = (x: Int) => (x < 3)
      val p2 = (x: Int) => (x > 3)
      val a = forall(u12, p1)
      val b = forall(u12, p2)
      val c = forall(u23, p1)
      assert(a, "forall elements in set {1, 2}. < 3 predicate is true")
      assert(!b, "forall elements in set {1, 2}. > 3 predicate is false")
      assert(!c, "forall elements in set {2, 3}. < 3 predicate is false")
    }
  }

  test("exists - returns true if atleast one element in S satisfies predicate p") {
    new TestSets {
      val p1 = (x: Int) => (x < 3)
      val p2 = (x: Int) => (x > 3)
      val a = exists(u12, p1)
      val b = exists(u12, p2)
      val c = exists(u23, p1)
      //assert(a, "There exists at least an element in set {1, 2} which is < 3")
      //assert(!b, "There does not exist at least an element in set {1, 2} which is > 3")
      //assert(!c, "There does not exist at least an element in set {2, 3} which is > 3")
    }
  }

  test("map - run map function on a set") {
    new TestSets {
      val f1 = (x: Int) => x * x
      val f2 = (x: Int) => x + 2
      val f3 = (x: Int) => x - 1
      //val s1 = map(u12, f1)
      //val s2 = map(u23, f2)
      val a = forall(map(u12, f1), u14)
      val b = forall(map(u23, f2), u45)
      val c = forall(map(u23, f3), u12)
      val d = forall(map(u12, f3), u01)
      assert(a, "the square function for map works fine")
      assert(b, "the +2 function for map works fine")
      assert(c, "the -1 function for map works fine")
      assert(d, "the -1 function for map works fine")
    }
  }
  
}
