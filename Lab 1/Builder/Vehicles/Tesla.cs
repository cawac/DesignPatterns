namespace Builder.Instances.Vehicles;

public class Tesla : IVehicle
{
    public double Weight { get; set; } = 1800;
    public double Length { get; set; } = 4.7;
    public double MaxSpeed { get; set; } = 250;
    public EWheelDriveType WheelDriveType { get; set; } = EWheelDriveType.Back;
    public EVehicleClass VehicleClass { get; set; } = EVehicleClass.Coupe;
    public EColor Color { get; set; } = EColor.Blue;
}
