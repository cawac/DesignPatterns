namespace AbstractFactory;

public interface ICreature
{
    public int MaxHealth { get; set; }
    public int Health { get; set; }
    public int Damage { get; set; }
    public int Armor { get; }
    public void TakeDamage(int damage);
    public void Attack(ref ICreature target);
}