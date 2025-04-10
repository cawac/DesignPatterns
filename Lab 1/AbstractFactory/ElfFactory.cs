namespace AbstractFactory;

public class ElfFactory: IAbstractFactory
{
    public ISolider CreateSolider()
    {
        return new ElfSolider();
    }

    public IRanger CreateRanger()
    {
        return new ElfRanger();
    }

    public IMagician CreateMagician()
    {
        return new ElfMagician();
    }

    public ICreature[] CreateSmallArmy()
    {
        ICreature[] army = new ICreature[25];
        
        for (int i = 0; i < 10; i++)
        {
            army[i] = this.CreateSolider();
        }

        for (int i = 10; i < 20; i++)
        {
            army[i] = this.CreateRanger();
        }

        for (int i = 20; i < 25; i++)
        {
            army[i] = this.CreateMagician();
        }

        return army;
    }

    public ICreature[] CreateBigArmy()
    {
        ICreature[] army = new ICreature[100];
        
        for (int i = 0; i < 40; i++)
        {
            army[i] = this.CreateSolider();
        }

        for (int i = 40; i < 90; i++)
        {
            army[i] = this.CreateRanger();
        }

        for (int i = 90; i < 100; i++)
        {
            army[i] = this.CreateMagician();
        }

        return army;
    }
}