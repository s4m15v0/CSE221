import java.util.*;

public class Task3 {
   public static void main(String[] args) {
       Scanner scan = new Scanner(System.in);
       
       String input1 = scan.nextLine();
       String input2 = scan.nextLine();
       String input3 = scan.nextLine();
      
       Comparator<Integer> COM = new Comparator<Integer>() {
            public int compare(Integer LHS, Integer RHS) {
                if (LHS < RHS)
                   return +1;
                if (LHS.equals(RHS))
                   return 0;
                return -1;
            }
        };
        
        PriorityQueue<Integer> MAXPQ = new PriorityQueue<Integer>(COM);
      
        
        String[] xy = input2.split(" ");
        
        int[] tasks = new int[xy.length];
        for(int i=0; i<xy.length; i++) {
           tasks[i] = Integer.parseInt(xy[i]);
        }
        Arrays.sort(tasks);
      
        int jackHours = 0, jillHours = 0;           
        int currentIndex = 0;                           
        
        for(int i=0; i<input3.length(); i++) {
           if(input3.charAt(i)=='J') {
               jackHours += tasks[currentIndex];       
               System.out.print(tasks[currentIndex]);   
               MAXPQ.add(tasks[currentIndex]);           
               currentIndex++;                           
           }
           else {
               int t = MAXPQ.poll();
               System.out.print(t);    
               jillHours += t;           
           }
        }
        System.out.println();
        System.out.println("Jack will work for " + jackHours + " hrs");
        System.out.println("Jill will work for " + jillHours + " hrs");
   }
}