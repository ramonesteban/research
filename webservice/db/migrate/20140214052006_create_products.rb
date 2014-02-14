class CreateProducts < ActiveRecord::Migration
  def change
    create_table :products do |t|
      t.string :name
      t.string :company
      t.string :origin
      t.string :description
      t.integer :rate

      t.timestamps
    end
  end
end
