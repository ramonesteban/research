class Product < ActiveRecord::Base
  validates :name,
    presence: true,
    length: { minimum: 2, maximum: 40 }

  validates :company,
    presence: true

  validates :origin,
    presence: true

  validates :description,
    presence: true

  validates :rate,
    presence: true

  def self.search(search)
    if search
      where('description LIKE ?', "%#{search}%")
    else
      all
    end
  end
end
