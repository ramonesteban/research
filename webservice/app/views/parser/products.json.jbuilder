json.array!(@products) do |product|
  json.extract! product, :id, :name, :company, :origin, :description, :rate
end
