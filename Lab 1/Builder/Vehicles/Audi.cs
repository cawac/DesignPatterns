namespace Builder.Instances.Vehicles;

public class Audi : IVehicle
{
    public double Weight { get; set; } = 1500;
    public double Length { get; set; } = 4.5;
    public double MaxSpeed { get; set; } = 240;
    public EWheelDriveType WheelDriveType { get; set; } = EWheelDriveType.All;
    public EVehicleClass VehicleClass { get; set; } = EVehicleClass.Sedan;
    public EColor Color { get; set; } = EColor.Red;
}