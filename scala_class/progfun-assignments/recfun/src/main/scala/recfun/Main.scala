package recfun
import common._

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = 
    if ((c == 0) || (c == r)) 1
    else pascal(c-1, r-1) + pascal(c, r-1)

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {
    def balance_helper1(chars: List[Char], sum: Int): Int = {
      var sum1 = sum 
      if (chars.isEmpty) 0
  	  else {
  	    sum1 = sum1 + balance_helper(chars.head)
  	    if (sum1 < 0) sum1
  	    else balance_helper(chars.head) + balance_helper1(chars.tail, sum1)
  	  }
    }
    def balance_helper(char: Char): Int =
      if (char == '(') 1 
      else if (char == ')') -1
      else 0
    
    balance_helper1(chars, 0) == 0
  }
  
  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    var count = 0
    count
  }
  
}
