package banking;

import java.util.HashMap;

public class Bank {
    HashMap<String, Account> accounts = new HashMap<>();

    public void openAccount(String id, double initialDeposit) throws InvalidAccountException {
        if(id == "" || accounts.containsKey(id)) 
            throw new InvalidAccountException();

        accounts.put(id, new Account(id, initialDeposit));
    }

    public Account getAccount(String id) throws InvalidAccountException {
        if(!accounts.containsKey(id)) 
            throw new InvalidAccountException();

        return accounts.get(id);
    }

    public void transfer(String fromId, String toId, double amount)
            throws InvalidAccountException, InsufficientFundsException {
        Account fromAcc = getAccount(fromId);
        Account toAcc = getAccount(toId);

        fromAcc.withdraw(amount);
        toAcc.deposit(amount);
    }
}
