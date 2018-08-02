import java.util.Collections;
import java.util.PriorityQueue;

public class UnionDifferenceIntersection {

  public static void main(String[] args) {
    PriorityQueue<String> queue1 = new PriorityQueue<String>();
    queue1.offer("George");
    queue1.offer("Jim");
    queue1.offer("John");
    queue1.offer("Blake");
    queue1.offer("Kevin");
    queue1.offer("Michael");
    
    System.out.println("This is queue1:");
    System.out.println(queue1);
      
    PriorityQueue<String> queue2 = new PriorityQueue<String>(4 ,
        Collections.reverseOrder());
    queue2.offer("Katie");
    queue2.offer("Kevin");
    queue2.offer("Michelle");
    queue2.offer("Ryan");
    
    System.out.println("This is queue2:");
    System.out.println(queue2);  
      
    //Union
    PriorityQueue<String> unionQueue = new PriorityQueue<String>(queue1.size() + queue2.size());
    unionQueue.addAll(queue1);
    unionQueue.addAll(queue2);
    
    System.out.println("\nThis is the union of queue1 and queue2:");
    System.out.println(unionQueue);
    
    //Intersection
    PriorityQueue<String> intersectQueue = new PriorityQueue<String>(queue1.size() + queue2.size());
    intersectQueue.addAll(queue1);
    intersectQueue.retainAll(queue2);
    
    System.out.println("\nThis is the intersection of queue1 and queue2:");
    System.out.println(intersectQueue);
    
    //Difference
    PriorityQueue<String> differenceQueue = new PriorityQueue<String>(queue1.size() + queue2.size());
    differenceQueue.addAll(queue1);
    differenceQueue.removeAll(queue2);
    
    System.out.println("\nThis is the difference of queue1 and queue2:");
    System.out.println(differenceQueue);
  }
  
}
