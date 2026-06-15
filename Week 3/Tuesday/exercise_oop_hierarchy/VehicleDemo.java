import java.util.ArrayList;
import java.util.List;

public class VehicleDemo {
    public static void main(String[] args) {
        List<Vehicle> fleet = new ArrayList<>();
        fleet.add(new GasCar("Ford", "Edge", 2018, 5.1, 1.16));
        fleet.add(new ElectricCar("Tesla", "Y", 2020, 17, 0.23));
        fleet.add(new GasCar("Honda", "Civic", 2015, 4.9, 1.20));
        fleet.add(new ElectricCar("Tesla", "X", 2021, 16, 0.22));


        
        for(int i = 0; i < fleet.size(); i++) {
            Vehicle v = fleet.get(i);
            System.out.println(v.getMake() + " " + v.getModel() + " fuel cost per 100km: " + v.fuelCostPer100Km());

            if(v instanceof AutonomousCapable) {
                System.out.println(v.getMake() + " " + v.getModel() + " is also autonomous capable!");
            }
        }
    }
}
