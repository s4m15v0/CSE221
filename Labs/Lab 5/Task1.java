import java.util.*;

public class Task1 {
   public static void main(String[] args) {
   
       Scanner scan = new Scanner(System.in);
      	 int n = scan.nextInt();
      	 int arr[][] = new int[n][2];
       for(int x=0; x<n; x++){
       arr[x][0] = scan.nextInt();
       arr[x][1] = scan.nextInt();
       }
       
       Arrays.sort(arr,new Comparator<int[]>(){
       public int compare(int arr1[],int arr2[]){
      	 int A1 = arr1[1];
      	 int A2 = arr2[1];
       	return String.valueOf(A1).compareTo(String.valueOf(A2));
      		 }
     	  }
       );

       ArrayList<Integer> index = new ArrayList<>();
      	 int R = 1;
      	 int f = arr[0][1];
       
      	 for(int y=1; y<n; y++){
     	  if(arr[y][0]>=f){
    	   R++;
      	 f = arr[y][1];
       index.add(y);
     	  }
       }

       System.out.println(R);
       System.out.println(arr[0][0]+" "+arr[0][1]);
      	 for(int z=0; z<index.size(); z++){
      	 System.out.println(arr[index.get(z)][0]+" "+arr[index.get(z)][1]);
       }
   }
}