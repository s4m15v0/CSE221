import java.util.*;

public class Task2 {
        public static void sort(Task[] tasks, int T) { //ascending order array sorting
                for (int x = 0; x < T; x++) {
                        for (int y = 0; y < T - 1; y++) {
                                if (tasks[y].finish > tasks[y + 1].finish) {
                                        // swap
                                        Task temp = new Task(tasks[y].start, tasks[y].finish);
                                        tasks[y] = tasks[y + 1];
                                        tasks[y + 1] = temp;
                                }
                        }
                }
        }
        public static int maxTaskCompletion(Task[] tasks, int N, int M) { //checking task is finished or ot 
            boolean taskDone[] = new boolean[N];

            int totalTasks = 0; //total task
            for (int z = 0; z < M; z++) {
                    int currentFinish = -1;
                    for (int k = 0; k < N; k++) {
                            if (!taskDone[k]) {
                                    if (tasks[k].start >= currentFinish) {
                                            currentFinish = tasks[k].finish;
                                            taskDone[k] = true;
                                            totalTasks++;
                                    }
                            }
                    }
            }

            return totalTasks;
    }
        
        public static void main(String[] args) {    //taking inputs  
            Scanner scan = new Scanner(System.in);
            int A = scan.nextInt(), 
            		B = scan.nextInt(); 
            Task tasks[] = new Task[A]; 
            for (int i = 0; i < A; i++) {
                    int F = scan.nextInt(), G = scan.nextInt();
                    tasks[i] = new Task(F, G);
            }
            sort(tasks, A);
            System.out.println(maxTaskCompletion(tasks, A, B));
    }
}

class Task {
    public int start, finish;
    public Task(int S_tart, int F_inish) {
            start = S_tart;
            finish = F_inish;
    }
}