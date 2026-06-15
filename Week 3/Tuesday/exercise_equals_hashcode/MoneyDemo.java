import java.util.HashSet;
import java.util.Set;

public class MoneyDemo {
    public static void main(String[] args) {
        // TODO: build Money USD 1000 cents twice, add to HashSet, print size
        // TODO: print equals vs ==
        Money m1 = new Money("USD", 1000);
        Money m2 = new Money("USD", 1000);

        HashSet<Money> hash = new HashSet();
        hash.add(m1);
        hash.add(m2);
        System.out.println("HashSet size: " + hash.size());
        System.out.println("Attempting m1.equals(m2), Result: " + m1.equals(m2));
        System.out.println("Attempting m1 == m2, Result: " + (m1 == m2));

        // If two objects are equal, hashCode() must match.
    }
}
