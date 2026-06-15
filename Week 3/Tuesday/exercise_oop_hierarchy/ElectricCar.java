public class ElectricCar extends Vehicle implements AutonomousCapable {
    // TODO fields: e.g. kWhPer100Km, pricePerKWh
    private double kWhPer100Km;
    private double pricePerKWh;

    public ElectricCar(String make, String model, int year, double kWhPer100Km, double pricePerKWh) {
        super(make, model, year);
        this.kWhPer100Km = kWhPer100Km;
        this.pricePerKWh = pricePerKWh;
    }

    @Override
    public double fuelCostPer100Km() {
        return kWhPer100Km * pricePerKWh;
    }

    public boolean supportsSelfDrive() {
        return true;
    }
}
