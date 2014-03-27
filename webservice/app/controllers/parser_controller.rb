class ParserController < ApplicationController
  def product
    product = params[:id]
    @product = Product.find_by(id: product)
    json_string = render_to_string(formats: :json)
    json_object = JSON.parse(json_string)
    render json: JSON.pretty_generate(json_object)
  end

  def products
    if params[:search].nil?
      @products = Product.all
    else
      @products = Product.search(params[:search])
    end
    json_string = render_to_string(formats: :json)
    json_object = JSON.parse(json_string)
    render json: JSON.pretty_generate(json_object)
  end

  def script
    value = %x(python --version 2>&1)
    path = Rails.root.join('public').to_s
    response = %x(python #{path}/ocr.py)
    render text: response
  end

  def new
    @product = Product.new(product_params)
    respond_to do |format|
      if @product.save
        format.html { redirect_to api_product_path(@product) }
      else
        format.html { render json: @product.errors }
      end
    end
  end

  private
    def product_params
      params.permit(:name, :company, :origin, :description, :rate)
    end
end
