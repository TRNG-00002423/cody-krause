package banking;

public class Account {
    private String id;
    private double balance;

    public Account(String id) {
        this.id = id;
        this.balance = 0.0;
    }

    public Account(String id, double balance) {
        this.id = id;
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount <= 0) 
            throw new IllegalArgumentException("Deposit amount cannot be less than or equal to 0");

        balance += amount;
    }

    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount <= 0) 
            throw new IllegalArgumentException("Withdraw amount cannot be less than or equal to 0");

        if (balance - amount < 0)
            throw new InsufficientFundsException("Not enough money in account to withdraw.");

        balance -= amount;
    }
}
