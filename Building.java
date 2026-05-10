/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package carbonfootprints;

/**
 *
 * @author JONATHAN
 */
public class Building implements CarbonFootprint{
    private String name;
    private double monthlyElectricity; // Consumo eléctrico
    private double monthlyGas; // Consumo gas
    
    public Building(String name, double monthlyElectricity, double monthlyGas){
        this.name = name;
        this.monthlyElectricity = monthlyElectricity;
        this.monthlyGas = monthlyGas;
    }
    
    @Override
    public double getCarbonFootprint() {
        // Cálculo electricidad: 0.233 kg CO2 por kWh
        // Cálculo gas: 1.9 kg CO2 por m^3
        double electricityEmissions = monthlyElectricity * 0.233;                
        double gasEmissions = monthlyGas * 1.9;
        return electricityEmissions + gasEmissions;
    }

    public String getName() {
        return name;
    }
    
}
