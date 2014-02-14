if !@product.nil?
  json.extract! @product, :name, :description, :rate
else
  json.status 'error'
  json.message 'not a valid product'
end
