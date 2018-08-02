import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Course {

    private String courseName;
    private int numberOfStudents;
    private String courseLecturer;

    public static void main (String[] args) {

        List<Course> Courses1 = new ArrayList<>();

        Courses1.add(new Course("Java", 23, "Robert"));
        Courses1.add(new Course("Python", 16, "Andy"));
        Courses1.add(new Course("C++", 21, "Zacharia"));
        Courses1.add(new Course("Ruby", 32, "Mark"));
        Courses1.add(new Course("C", 5, "Binu"));

        System.out.println("Before sorting: " + Courses1);
        Collections.sort(Courses1, new CourseStuNumComparator());
        System.out.println("After Sorting: " + Courses1);
        Collections.swap(Courses1, 1, 2);
        System.out.println("After Swap: " + Courses1);

        List<Course> Courses2 = new ArrayList<>();

        Collections.addAll(Courses2, new Course("English", 7, "Angela"),
                new Course("German", 12, "Heather"),
                new Course("Spanish", 14, "Sofia"),
                new Course("Portuguese", 17, "Maria"),
                new Course("Mandarin", 25, "Julissa"));
        System.out.println("Add all to Courses2: " + Courses2);

        Collections.copy(Courses2, Courses1);
        System.out.println("Copy Courses 1 to Courses 2: " + Courses2);

        Courses2.add(new Course("Java101", 55, "Dr. P Green"));
        Courses2.add(new Course("Advanced Programming", 93, "Prof. M Milton"));

        Collections.sort(Courses2, new CoursesNameComparator());
        System.out.println("Courses2 ordered by Name: " + Courses2);

        int index = Collections.binarySearch(Courses2,
                new Course("Java101", 0, null), new CoursesNameComparator());
        System.out.println("Java101 in List is at: " + index );

        System.out.println("Disjoint between Courses1 and Courses2: " + Collections.disjoint(Courses1, Courses2));

        System.out.println("The course with the most students is: " + Collections.max(Courses2, new CourseStuNumComparator()));
        System.out.println("The course with the least students is: " + Collections.min(Courses2, new CourseStuNumComparator()));
    }

    public Course(String crse_nme, int num_stu, String crse_lect) {

        courseName = crse_nme;
        numberOfStudents = num_stu;
        courseLecturer = crse_lect;
    }

    public String getCourseName() {
        return courseName;
    }

    public int getNumStudents() {
        return numberOfStudents;
    }

    public String toString() {
        return String.format("(%s, %s, %d", courseName, courseLecturer, numberOfStudents);
    }

    static class CourseStuNumComparator implements Comparator<Course> {
        @Override
        public int compare(Course course1, Course course2) {
            return course1.getNumStudents() - course2.getNumStudents();
        }
    }

    static class CoursesNameComparator implements Comparator<Course> {
        @Override
        public int compare(Course course1, Course course2) {
            return course1.getCourseName().compareTo(course2.getCourseName());
        }
    }
}
