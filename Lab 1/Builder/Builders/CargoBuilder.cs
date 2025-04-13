namespace Builder;

public class CargoBuilder: IBuilder<Cargo>
{
    protected Cargo? Car { get; set; }
    
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
            this.Car = new Cargo
            {
                Name = name,
                Weight = weight,
                Length = length,
                MaxSpeed = maxSpeed
            };
        }
    }
    
    public void BuildSpecific(double tonnage, double tankVolume, int axlesAmount)
    {
        if (this.Car == null)
        {
            return;
        }
        this.Car.Tonnage = tonnage;
        this.Car.TankVolume = tankVolume;
        this.Car.AxlesAmount = axlesAmount;
    }

    public Cargo? GetResult()
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