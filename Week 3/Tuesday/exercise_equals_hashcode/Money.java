import java.util.Objects;

/**
 * TODO: immutable currency + amountMinor; equals/hashCode contract.
 */
public final class Money {
    // TODO fields, constructor validates currency non-null
    private String currency;
    private long amountMinor;

    public Money(String currency, long amountMinor) {
        if(currency == null) {
            throw new IllegalArgumentException("Currency cannot be null.");
        } else {
            this.currency = currency;
        }

        this.amountMinor = amountMinor;
    }

    // TODO getters
    public String getCurrency() {
        return currency;
    }

    public long getAmountMinor() {
        return amountMinor;
    }

    @Override
    public boolean equals(Object o) {
        if(o == null || o.getClass() != getClass()) {
            return false;
        }

        Money other = (Money)o;
        if(other.getCurrency() == getCurrency() && other.getAmountMinor() == getAmountMinor()) {
            return true;
        } else {
            return false;
        }
    }

    @Override
    public int hashCode() {
        return Objects.hash(currency, amountMinor);
    }

    @Override
    public String toString() {
        return amountMinor + " of " + currency;
    }
}
