public class GasCar extends Vehicle {
    // TODO fields: e.g. litersPer100Km, pricePerLiter
    private double litersPer100Km;
    private double pricePerLiter;

    public GasCar(String make, String model, int year, double litersPer100Km, double pricePerLiter) {
        super(make, model, year);
        this.litersPer100Km = litersPer100Km;
        this.pricePerLiter = pricePerLiter;
    } 

    @Override
    public double fuelCostPer100Km() {
        return litersPer100Km * pricePerLiter;
    }
}
