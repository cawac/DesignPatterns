namespace AbstractFactory;

public interface IMagician: ICreature
{
    void Heal(ref ICreature target);
}