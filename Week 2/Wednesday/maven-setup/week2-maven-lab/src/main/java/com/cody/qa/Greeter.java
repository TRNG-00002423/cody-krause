package com.cody.qa;

public class Greeter {
    public String hello(String name) {
        if (name.equals("")) {
            throw new IllegalArgumentException("Cannot input empty string into function.");
        }
        
        return "Hello, " + name;
    }
}
