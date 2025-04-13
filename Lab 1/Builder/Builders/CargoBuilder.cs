using Builder.Instances;

namespace Builder;

public class CargoBuilder: IBuilder<ICargo>
{
    protected ICargo? Car { get; set; }

    public void Build(double Tonnage, double TankVolume, int AxlesAmount)
    {
        if (AxlesAmount == 3)
        {
            this.Car = new Scania();
        }
        else if (AxlesAmount == 4)
        {
            this.Car = new Man();
        }
        else if (AxlesAmount == 5)
        {
            this.Car = new Volvo();
        }
    }
    
    public ICargo? GetResult()
    {
        return this.Car;
    }

    public void Reset()
    {
        return;
    }
}