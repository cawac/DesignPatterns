using Builder.Instances.Tanks;

namespace Builder;

public class TankBuilder: IBuilder<ITank>
{
    protected ITank? Car { get; set; } = null;
    
    public void Build(int CrewSize, double ProjectileCaliber, int ShotsPerMinute)
    {
        if (CrewSize == 5)
        {
            this.Car = new Tiger();
        }
        else if (CrewSize == 4)
        {
            this.Car = new Merkava();
        }
        else if (CrewSize == 3)
        {
            this.Car = new Abrams();
        }
    }
    
    public ITank? GetResult()
    {
        return Car;
    }

    public void Reset()
    {
        return;
    }
}