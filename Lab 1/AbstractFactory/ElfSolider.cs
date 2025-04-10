namespace AbstractFactory;

public class ElfSolider: ISolider
{
    public int MaxHealth { get; set; } = 150;
    public int Health { get; set; } = 100;
    public int Damage { get; set; } = 20;
    public int Armor { get; } = 5;
    public void TakeDamage(int damage)
    {
        this.Health -= damage - this.Armor;
    }

    public void Attack(ref ICreature target)
    {
        target.TakeDamage(this.Damage);
    }
}