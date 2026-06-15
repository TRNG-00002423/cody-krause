/** Lab 2 driver — run after Student is implemented. */
public class StudentDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Cody", "Computer Science");
        Student s2 = new Student("Mary", "Mathematics");
        Student s3 = new Student("Sam", "Geology");
        Student s4 = new Student("Cody", "Computer Science");

        Student[] students = {s1,s2,s3,s4};

        System.out.println("Students: ");
        for(int i = 0; i < students.length; i++) {
            System.out.println((i+1) + ". " + students[i]);
        }

        System.out.println("\nEnrollment Count: " + Student.getEnrollmentCount());
        System.out.println("Trying to compare Student with id 0 to Student with id 3...");
        System.out.println("Result: " + (s1.equals(s4)));
        System.out.println("'equals' compares using values while '==' compares object identity (such as memory address)");
    }
}
