namespace Builder;

public class TankBuilder: IBuilder<Tank>
{
    protected Tank? Car { get; set; }
    
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
            this.Car = new Tank
            {
                Name = name,
                Weight = weight,
                Length = length,
                MaxSpeed = maxSpeed
            };
        }
    }
    
    public void BuildSpecific(double projectileCaliber, int shotsPerMinute, int crewSize)
    {
        if (this.Car == null)
        {
            return;
        }
        this.Car.ProjectileCaliber = projectileCaliber;
        this.Car.ShotsPerMinute = shotsPerMinute;
        this.Car.CrewSize = crewSize;
    }

    public Tank? GetResult()
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