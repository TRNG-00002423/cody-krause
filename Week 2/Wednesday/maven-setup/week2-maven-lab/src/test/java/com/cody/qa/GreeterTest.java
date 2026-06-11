package com.cody.qa;

import org.junit.Assert;
import org.junit.Test;

public class GreeterTest {
    
    @Test
    public void helloTest() {
        Greeter g = new Greeter();

        String expectedResult = "Hello, Cody";
        String actualResult = g.hello("Cody");

        Assert.assertEquals(expectedResult, actualResult);
    }

    @Test
    public void helloTest2() {
        Greeter g = new Greeter();
        boolean errorThrown = false;

        try {
            String result = g.hello("");
        } catch (IllegalArgumentException e) {
            errorThrown = true;
        }

        Assert.assertTrue(errorThrown);
    }
}
