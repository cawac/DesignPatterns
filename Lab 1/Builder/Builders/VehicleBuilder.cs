namespace Builder;

public class VehicleBuilder: IBuilder<Vehicle>
{
    protected Vehicle? Car { get; set; }
    
    public void BuildBase(string name, double weight, double length, double maxSpeed)
    {
        if (Car != null)
        {
            Car.Name = name;
            Car.Weight = weight;
            Car.Length = length;
            Car.MaxSpeed = maxSpeed;
        }
        else
        {
            this.Car = new Vehicle
            {
                Name = name,
                Weight = weight,
                Length = length,
                MaxSpeed = maxSpeed
            };
        }
    }
    
    public void BuildSpecific(EWheelDriveType wheelDriveType, EVehicleClass vehicleClass, EColor color)
    {
        if (this.Car == null)
        {
            return;
        }
        this.Car.WheelDriveType = wheelDriveType;
        this.Car.VehicleClass = vehicleClass;
        this.Car.Color = color;
    }

    public Vehicle? GetResult()
    {
        var car = this.Car;
        this.Reset();
        return car;
    }

    public void Reset()
    {
        this.Car = null;
    }
}