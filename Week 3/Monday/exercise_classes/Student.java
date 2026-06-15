import java.util.Objects;

/**
 * Lab 2 — Student. Replace UnsupportedOperationException bodies with real logic.
 * See ../README.md
 */
public class Student {
    // TODO: private static nextId, private static count of instances
    // TODO: private final int id; private String name; private String program
    private static int nextId = 0;
    private static int instanceCount = 0;
    private final int id;
    private String name;
    private String program;

    public Student(String name, String program) {
        this.name = name;
        this.program = program;
        id = nextId;
        nextId++;
        instanceCount++;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getProgram() {
        return program;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setProgram(String program) {
        this.program = program;
    }

    public static int getEnrollmentCount() {
        return instanceCount;
    }

    @Override
    public String toString() {
        return "Student [name: " + name + ", id: " + id + ", program: " + program + "]";
    }

    @Override
    public boolean equals(Object o) {
        if(o == null || o.getClass() != getClass()) {
            return false;
        }

        Student other = (Student)o;
        if(other.id == id) {
            return true; 
        } else {
            return false;
        }
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, id, program);
    }
}
