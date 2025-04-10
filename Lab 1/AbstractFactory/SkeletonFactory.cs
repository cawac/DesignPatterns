namespace AbstractFactory;

public class SkeletonFactory: IAbstractFactory
{
    public ISolider CreateSolider()
    {
        return new SkeletonSolider();
    }

    public IRanger CreateRanger()
    {
        return new SkeletonRanger();
    }

    public IMagician CreateMagician()
    {
        return new SkeletonMagician();
    }

    public ICreature[] CreateSmallArmy()
    {
        ICreature[] army = new ICreature[50];
        
        for (int i = 0; i < 30; i++)
        {
            army[i] = this.CreateSolider();
        }

        for (int i = 30; i < 45; i++)
        {
            army[i] = this.CreateRanger();
        }

        for (int i = 45; i < 50; i++)
        {
            army[i] = this.CreateMagician();
        }

        return army;
    }

    public ICreature[] CreateBigArmy()
    {
        ICreature[] army = new ICreature[200];
        
        for (int i = 0; i < 120; i++)
        {
            army[i] = this.CreateSolider();
        }

        for (int i = 120; i < 180; i++)
        {
            army[i] = this.CreateRanger();
        }

        for (int i = 180; i < 200; i++)
        {
            army[i] = this.CreateMagician();
        }

        return army;
    }
}